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

    def filterEntriesByAttribute(self, attribute, value):
        filteredList = [
            vehicle for vehicle in self._vehicles if vehicle[attribute] == value]
        self.displayEntries(filteredList)

    def loadEntriesFromFile(self, filePath):
        self._vehicles = pickle.load(open(filePath, "rb"))
        idList = [vehicle["id"] for vehicle in self._vehicles]
        self._id_counter = max(idList)

def main():
    vehicleDB = VehicleDatabase()
    vehicleDB.addEntries()
    vehicleDB.displayEntries()
    print("\nSorted by mileage : ")
    vehicleDB.sortEntriesByMileage()
    print("\nDeleted entry with ID 2 : ")
    vehicleDB.deleteEntry(2)
    vehicleDB.displayEntries()
    print("\nModified entry with ID 3 : ")
    vehicleDB.modifyEntry(3, "model", "Accord")
    vehicleDB.displayEntries()
    print("\nFiltered by vendor : ")
    vehicleDB.filterEntriesByAttribute("vendor", "Swift")
    vehicleDB.createPickleFile()
    vehicleDB.generateReport("vehicleDetails.pdf")

if __name__ == "__main__":
    main()