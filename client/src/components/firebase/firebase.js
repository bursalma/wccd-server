import app from 'firebase/app'
import 'firebase/auth';

const config = {
    apiKey: "AIzaSyBDgcdcEPZrU4vuuJ8QfEpxnTGCNJ0Y5J8",
    authDomain: "white-collar-cc7d8.firebaseapp.com",
    databaseURL: "https://white-collar-cc7d8.firebaseio.com",
    projectId: "white-collar-cc7d8",
    storageBucket: "white-collar-cc7d8.appspot.com",
    messagingSenderId: "16623267809",
    appId: "1:16623267809:web:73721030c78e3641ba6ca0"
};

class Firebase {
    constructor() {
        app.initializeApp(config)

        this.auth = app.auth();
    }

    doCreateUserWithEmailAndPassword = (email, password) =>
        this.auth.createUserWithEmailAndPassword(email, password);
    
    doSignInWithEmailAndPassword = (email, password) =>
        this.auth.signInWithEmailAndPassword(email, password);

    doSignOut = () => 
        this.auth.signOut();

    doPasswordReset = email =>
        this.auth.sendPasswordResetEmail(email);

    doPasswordUpdate = password =>
        this.auth.currentUser.updatePassword(password);
}

export default Firebase;