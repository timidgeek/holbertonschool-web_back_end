// link routes to app controller and students controller
import app from '../server';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

app.get('/', (req, res) => {
  res.send(AppController.getHomepage());
});

app.get('/students:major', (req, res) => {
  const major = req.params.major;
  if (major === 'CS' || major === 'SWE') {
    res.send(StudentsController.getAllStudentsByMajor(req));
  } else {
    res.send(StudentsController.getAllStudents());
  }
});
