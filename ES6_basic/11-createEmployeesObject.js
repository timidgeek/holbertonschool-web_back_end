export default function createEmployeesObject(departmentName, employees) {
  const companyInfo = {
    [departmentName]:
            employees,

  };

  return companyInfo;
}
