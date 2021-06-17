class Employee {
    empID: number;
    empName: string;

    constructor(ID: number, name: string) {
        this.empName = name;
        this.empID = ID;
    }

    getSalary(): number {
        return 40000;
    }
}

var employee: Employee;
employee = new Employee(123, "Dylan Thiemann");

console.log(employee.getSalary());