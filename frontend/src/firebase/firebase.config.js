// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBs_9dsYiDN16wGw8Tm3EwqperjpUxY--M",
  authDomain: "g5-arquitectura.firebaseapp.com",
  projectId: "g5-arquitectura",
  storageBucket: "g5-arquitectura.appspot.com",
  messagingSenderId: "734139387824",
  appId: "1:734139387824:web:7dba57e18a3447f24ad075",
  measurementId: "G-707LK21PSY"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);