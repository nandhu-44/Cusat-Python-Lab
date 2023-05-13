from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.messagebox import showinfo
from tkinter.ttk import Style, Treeview
import pickle
import tabulate
from fpdf import FPDF

class VehicleAttributes:
    _keys = ["id", "ownerName", "vendor", "model", "type",
             "registrationNumber", "engineNumber", "mileage"]
    _dataBase = dict.fromkeys(_keys, None)

class VehicleDatabase(VehicleAttributes):
    _vehicles = []
    _id_counter = 0
    def addEntries(self):
        entries = [
            [1, "Maruti Suzuki", "Swift", "Hatchback", 
                "Petrol", "MH01AB1234", "1234567890", 21.4],
            [2, "Hyundai", "Creta", "SUV", "Diesel", 
                "MH02CD5678", "0987654321", 17.1],
            [3, "Tata Motors", "Nexon", "SUV", "Petrol", 
                "MH03EF9012", "2345678901", 18.0]
        ]
        
        for entry in entries:
            self._id_counter += 1
            entry[0] = self._id_counter
            vehicle = dict(zip(self._dataBase.keys(), entry))
            self._vehicles.append(vehicle)

    def deleteEntry(self, vehicleId):
        for i in range(len(self._vehicles)):
            if self._vehicles[i]["id"] == vehicleId:
                del self._vehicles[i]
                break
        else:
            print("Invalid ID")

    def modifyEntry(self, vehicleId, attribute, value):
        found = False
        for vehicle in self._vehicles:
            if vehicle["id"] == vehicleId:
                if attribute in self._dataBase.keys():
                    vehicle[attribute] = value
                    found = True
                    break
                else:
                    print("Invalid attribute")
                    break
        if not found:
            print("Invalid ID")

    def generateReport(self, filename):
        pdf = FPDF()
        pdf.add_page()
        header = ["Id", "Owner", "Vendor", "Model", "Type",
                  "Registration Number", "Engine Number", "Mileage"]
        data = [list(vehicle.values()) for vehicle in self._vehicles]
        pdf.set_font("Arial", "B", 12)
        for col in header:
            pdf.cell(40, 10, col, 1, 0, "C")
        pdf.ln()
        pdf.set_font("Arial", "", 12)
        for row in data:
            for col in row:
                pdf.cell(40, 10, str(col), 1, 0, "C")
            pdf.ln()
        pdf.output(filename)

    def displayEntries(self, filteredList=None):
        header = ["Id", "Owner", "Vendor", "Model", "Type",
                  "Registration Number", "Engine Number", "Mileage"]
        rows = [x.values() for x in filteredList] if filteredList else [
            x.values() for x in self._vehicles]
        print(tabulate.tabulate(rows, header, tablefmt="grid"))

    def sortEntriesByMileage(self):
        sortedList = sorted(self._vehicles, key=lambda i: i["mileage"])
        self.displayEntries(sortedList)

    def createPickleFile(self):
        pickle.dump(self._vehicles, open("vehicleDetails.bin", "wb"))

class VehicleApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Vehicle Database")
        self.style = Style()
        self.style.theme_use("default")
        self.treeview = None
        self.db = VehicleDatabase()

    def create_treeview(self):
        self.treeview = Treeview(self.root)
        self.treeview["columns"] = (
            "Owner", "Vendor", "Model", "Type", "Registration Number", "Engine Number", "Mileage"
        )
        self.treeview.column("#0", width=50, minwidth=50, stretch=NO)
        self.treeview.column("Owner", width=100, minwidth=100, stretch=NO)
        self.treeview.column("Vendor", width=100, minwidth=100, stretch=NO)
        self.treeview.column("Model", width=100, minwidth=100, stretch=NO)
        self.treeview.column("Type", width=100, minwidth=100, stretch=NO)
        self.treeview.column("Registration Number", width=150, minwidth=150, stretch=NO)
        self.treeview.column("Engine Number", width=150, minwidth=150, stretch=NO)
        self.treeview.column("Mileage", width=100, minwidth=100, stretch=NO)
        self.treeview.heading("#0", text="ID", anchor=CENTER)
        self.treeview.heading("Owner", text="Owner", anchor=CENTER)
        self.treeview.heading("Vendor", text="Vendor", anchor=CENTER)
        self.treeview.heading("Model", text="Model", anchor=CENTER)
        self.treeview.heading("Type", text="Type", anchor=CENTER)
        self.treeview.heading("Registration Number", text="Registration Number", anchor=CENTER)
        self.treeview.heading("Engine Number", text="Engine Number", anchor=CENTER)
        self.treeview.heading("Mileage", text="Mileage", anchor=CENTER)
        self.treeview.pack(fill=BOTH, expand=YES)

    def populate_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        for vehicle in self.db._vehicles:
            self.treeview.insert("", END, text=str(vehicle["id"]), values=(
                vehicle["ownerName"],
                vehicle["vendor"],
                vehicle["model"],
                vehicle["type"],
                vehicle["registrationNumber"],
                vehicle["engineNumber"],
                vehicle["mileage"]
            ))

    def add_entry(self):
        new_entry = [
            None,
            self.owner_entry.get(),
            self.vendor_entry.get(),
            self.model_entry.get(),
            self.type_entry.get(),
            self.reg_num_entry.get(),
            self.engine_num_entry.get(),
            float(self.mileage_entry.get())
        ]
        self.db._id_counter += 1
        new_entry[0] = self.db._id_counter
        vehicle = dict(zip(self.db._dataBase.keys(), new_entry))
        self.db._vehicles.append(vehicle)
        self.populate_treeview()

    def delete_entry(self):
        selected_items = self.treeview.selection()
        if len(selected_items) == 0:
            showinfo("Error", "No entry selected.")
            return
        selected_id = int(self.treeview.item(selected_items[0], "text"))
        self.db.deleteEntry(selected_id)
        self.populate_treeview()

    def modify_entry(self):
        selected_items = self.treeview.selection()
        if len(selected_items) == 0:
            showinfo("Error", "No entry selected.")
            return
        selected_id = int(self.treeview.item(selected_items[0], "text"))
        modify_window = Toplevel(self.root)
        modify_window.title("Modify Entry")
        attr_label = Label(modify_window, text="Attribute:")
        attr_label.grid(row=0, column=0, padx=5, pady=5)
        attr_entry = Entry(modify_window)
        attr_entry.grid(row=0, column=1, padx=5, pady=5)
        value_label = Label(modify_window, text="New Value:")
        value_label.grid(row=1, column=0, padx=5, pady=5)
        value_entry = Entry(modify_window)
        value_entry.grid(row=1, column=1, padx=5, pady=5)

        def modify():
            attribute = attr_entry.get()
            value = value_entry.get()
            self.db.modifyEntry(selected_id, attribute, value)
            modify_window.destroy()
            self.populate_treeview()
        # Creating a button to modify the entry
        modify_button = Button(modify_window, text="Modify", command=modify)
        modify_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def generate_report(self):
        filename = asksaveasfile(mode="wb", defaultextension=".pdf")
        if filename is None:
            return
        self.db.generateReport(filename.name)
        showinfo("Success", "Report generated successfully.")

    def display_entries(self):
        self.db.displayEntries()

    def sort_entries(self):
        self.db.sortEntriesByMileage()

    def create_pickle_file(self):
        self.db.createPickleFile()
        showinfo("Success", "Pickle file created successfully.")

    def setup_ui(self):
        self.create_treeview()
        # Creating labels and entry fields
        owner_label = Label(self.root, text="Owner:")
        owner_label.pack()
        self.owner_entry = Entry(self.root)
        self.owner_entry.pack()
        vendor_label = Label(self.root, text="Vendor:")
        vendor_label.pack()
        self.vendor_entry = Entry(self.root)
        self.vendor_entry.pack()
        model_label = Label(self.root, text="Model:")
        model_label.pack()
        self.model_entry = Entry(self.root)
        self.model_entry.pack()
        type_label = Label(self.root, text="Type:")
        type_label.pack()
        self.type_entry = Entry(self.root)
        self.type_entry.pack()
        reg_num_label = Label(self.root, text="Registration Number:")
        reg_num_label.pack()
        self.reg_num_entry = Entry(self.root)
        self.reg_num_entry.pack()
        engine_num_label = Label(self.root, text="Engine Number:")
        engine_num_label.pack()
        self.engine_num_entry = Entry(self.root)
        self.engine_num_entry.pack()
        mileage_label = Label(self.root, text="Mileage:")
        mileage_label.pack()
        self.mileage_entry = Entry(self.root)
        self.mileage_entry.pack()
        add_button = Button(self.root, text="Add Entry", command=self.add_entry)
        add_button.pack(pady=5)
        delete_button = Button(self.root, text="Delete Entry", command=self.delete_entry)
        delete_button.pack(pady=5)
        modify_button = Button(self.root, text="Modify Entry", command=self.modify_entry)
        modify_button.pack(pady=5)
        generate_button = Button(self.root, text="Generate Report", command=self.generate_report)
        generate_button.pack(pady=5)
        display_button = Button(self.root, text="Display Entries", command=self.display_entries)
        display_button.pack(pady=5)
        sort_button = Button(self.root, text="Sort Entries by Mileage", command=self.sort_entries)
        sort_button.pack(pady=5)
        pickle_button = Button(self.root, text="Create Pickle File", command=self.create_pickle_file)
        pickle_button.pack(pady=5)

    def run(self):
        self.setup_ui()
        self.db.addEntries()
        self.populate_treeview()
        self.root.mainloop()

app = VehicleApp()
app.run()

