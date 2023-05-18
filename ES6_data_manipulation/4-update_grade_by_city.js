export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const newStudent = student;
      newStudent.grade = 'N/A';
      for (const list of newGrades) {
        if (newStudent.id === list.studentId) {
          newStudent.grade = list.grade;
        }
      }
      return newStudent;
    });
}
