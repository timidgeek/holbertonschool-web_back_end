export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const newTask = true;
    const newTask2 = false;
    return [newTask2, newTask];
  }

  return [task, task2];
}
