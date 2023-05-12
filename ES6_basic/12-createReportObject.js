import { departmentName, employees } from './11-createEmployeesObject';

export default function createReportObject(employeesList){
    return {
        allEmployees: {
            ...employeesList,
        },
        getNumberOfDepartments() {
            return Object.keys(employeesList).length;
        }
    };
}