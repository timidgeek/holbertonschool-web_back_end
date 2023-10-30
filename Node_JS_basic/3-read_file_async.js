// task three - asynch file read
const fs = require('fs');

module.exports = async function countStudents(path) {
  // gets info from `database.csv` asynchronously
  // returns a promise
  let db;
  try {
    db = await fs.promises.readFile(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  // parse the CSV data
  let data = db.split('\n');
  data = data.filter((line) => line !== '').slice(1);
  console.log(`Number of students: ${data.length}`);
  // iterate through field of study data with map()
  const field = data.map((line) => line.split(',')[3]);
  const eachField = [...new Set(field)];

  const dict = {};

  for (let i = 0; i < eachField.length; i += 1) {
    const numStudents = field.filter(
      (fieldName) => fieldName === eachField[i],
    ).length;

    const studentsPerField = data.filter(
      (line) => line.split(',')[3] === eachField[i],
    );

    const student = studentsPerField.map((line) => line.split(',')[0]);

    // log num students from each field with special format
    console.log(
      `Number of students in ${
        eachField[i]
      }: ${numStudents}. List: ${student.join(', ')}`,
    );
    // format data
    dict[eachField[i]] = {
      numStudents,
      student,
    };
  }
  return dict;
};
