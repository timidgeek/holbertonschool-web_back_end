import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const uploadPromise = uploadPhoto();
  const createPromise = createUser();

  return Promise.all([uploadPromise, createPromise])
    .then(([uploadResult, createResult]) => {
      console.log(uploadResult.body, createResult.firstName, createResult.lastName);
    })
    .catch(error => {
      console.log('Signup system offline');
      throw error;
    });
}
