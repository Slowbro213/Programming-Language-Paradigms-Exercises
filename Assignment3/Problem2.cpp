#include <iostream>

using namespace std;

class Computer;
class CPU {
private:
    int clockFrequency;
    std::string instructionSetArchitecture;
    int type;
    int numberOfRegisters;
    std::string manufacturer;

public:
    CPU(int cf, std::string isa, int t, int nor, std::string m)
        : clockFrequency(cf), instructionSetArchitecture(isa), type(t), numberOfRegisters(nor), manufacturer(m) {}

    friend ostream& operator<<(std::ostream& os, const CPU& obj) {
        os << "Clock Frequency: " << obj.clockFrequency << " Instruction Set Architecture: " << obj.instructionSetArchitecture << " Type: " << obj.type << " Number of Registers: " << obj.numberOfRegisters << " Manufacturer: " << obj.manufacturer;
        return os;
    }
};

class RAM {
private:
    int size;
    std::string type;
    std::string manufacturer;
public:
    RAM(int s, std::string t, std::string m) : size(s), type(t), manufacturer(m) {}
    friend ostream& operator<<(std::ostream& os, const RAM& obj) {
        os << "Size: " << obj.size << " Type: " << obj.type << " Manufacturer: " << obj.manufacturer;
        return os;
    }
};

class HardDisk {
private:
    int size;
    int rotationsPerMinute;
    string manufacturer;
public:
    HardDisk(int s, int rpm, std::string m) : size(s), rotationsPerMinute(rpm), manufacturer(m) {}
    friend ostream& operator<<(std::ostream& os, const HardDisk& obj) {
        os << "Size: " << obj.size << " Rotations Per Minute: " << obj.rotationsPerMinute << " Manufacturer: " << obj.manufacturer;
        return os;
    }
};

class Motherboard {
private:
    std::string chipsetVersion;
    int usbPortsNumber;
    int maxRAMCapacity;
    std::string manufacturer;
public:
    Motherboard(std::string cv, int upn, int mrc, std::string m)
        : chipsetVersion(cv), usbPortsNumber(upn), maxRAMCapacity(mrc), manufacturer(m) {}
    friend ostream& operator<<(std::ostream& os, const Motherboard& obj) {
        os << "Chipset Version: " << obj.chipsetVersion << " USB Ports Number: " << obj.usbPortsNumber << " Max RAM Capacity: " << obj.maxRAMCapacity << " Manufacturer: " << obj.manufacturer;
        return os;
    }
};

class Computer {
public:
    CPU cpu;
    RAM ram;
    HardDisk hardDisk;
    Motherboard motherboard;
    int year;
    double price;

    Computer(CPU c, RAM r, HardDisk hd, Motherboard m, int y, double p)
        : cpu(c), ram(r), hardDisk(hd), motherboard(m), year(y), price(p) {}
     friend ostream& operator<<(std::ostream& os, const Computer& obj) {
       cout << "CPU: " << obj.cpu << endl <<" RAM: " << obj.ram << endl <<" Hard Disk: " << obj.hardDisk << endl <<" Motherboard: " << obj.motherboard << endl <<" Year: " << obj.year << endl <<" Price: " << obj.price <<endl;
        return os;
    }
};

int main()
{
        /*CPU: 4 GHz, CISC, 32 bit, 32
    registers, INTEL
    RAM: 8 GB, DDR3, Producer Kingston
    Hard Hard Disk: 1000 GB, 7200 RPM,
    Seagate Motherboard: Chipset Intel Z77,
    6 USB ports, Max. 64 GB of RAM, MSI
    Year: 2018
    Price: 560.75*/
    CPU cpu(4, "CISC", 32, 32, "INTEL");
    RAM ram(8, "DDR3", "Kingston");
    HardDisk hardDisk(1000, 7200, "Seagate");
    Motherboard motherboard("Intel Z77", 6, 64, "MSI");
    Computer computer2(cpu, ram, hardDisk, motherboard, 2018, 560.75);
    cout << computer2<<endl;
        /*CPU: 3 GHz, CISC, 32 bit, 64 registers,
    AMD RAM: 4 GB, DDR2, Producer Kingston
    Hard Hard Disk: 500 GB, 7200 RPM,
    Maxtor Motherboard:, Chipset AMD970, 6
    USB ports, Max. 16 GB of RAM, AMD
    Year: 2019
    Price: 482.5*/
    CPU cpu1(3, "CISC", 32, 64, "AMD");
    RAM ram1(4, "DDR2", "Kingston");
    HardDisk hardDisk1(500, 7200, "Maxtor");
    Motherboard motherboard1("AMD970", 6, 16, "AMD");
    Computer computer1(cpu1, ram1, hardDisk1, motherboard1, 2019, 482.5);
    cout << computer1<<endl;
    return 0;
}