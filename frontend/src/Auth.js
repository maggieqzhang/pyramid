import React, { useEffect, useState} from 'react';

export const AuthContext = React.createContext();

export const AuthProvider = ({ children }) => {
    const [currentUser, setCurrentUser] = useState(null);

    const url = `http://127.0.0.1:5000/login`;
    const fetchLoginData = async () => {
        const res = await fetch(url);
        const loginJSON = await res.json();
        // setCurrentUser(loginJSON);
        console.log(res)
    };

    useEffect(() => {
        fetchLoginData()
    }, []);
    
    return (
        <AuthContext.Provider value={{currentUser}}>
            {children}
        </AuthContext.Provider>
    );
};