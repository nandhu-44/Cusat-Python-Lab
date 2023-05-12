import pickle
import tabulate


class VehicleAttributes:
    _keys = ["id", "ownerName", "vendor", "model", "type",
             "registrationNumber", "engineNumber", "mileage"]
    _dataBase = dict.fromkeys(_keys, None)


class VehicleDatabase(VehicleAttributes):
    _vehicles = []
    _id_counter = 0

    def addEntries(self):
        entries = [
            [1, "John Doe", "Ford", "Mustang", "Sedan", 1234, 5678, 25.5],
            [2, "Jane Smith", "Toyota", "Camry", "Sedan", 5678, 9012, 30.2],
            [3, "Bob Johnson", "Honda", "Civic", "Sedan", 9012, 3456, 27.8],
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

    print()
    print("Sorted by mileage : ")
    vehicleDB.sortEntriesByMileage()
    print()
    print("Deleted entry with ID 2 : ")
    vehicleDB.deleteEntry(2)
    vehicleDB.displayEntries()
    print()
    print("Modified entry with ID 3 : ")
    vehicleDB.modifyEntry(3, "model", "Accord")
    vehicleDB.displayEntries()
    print()
    print("Filtered by vendor : ")
    vehicleDB.filterEntriesByAttribute("vendor", "Honda")

    vehicleDB.createPickleFile()


if __name__ == "__main__":
    main()
