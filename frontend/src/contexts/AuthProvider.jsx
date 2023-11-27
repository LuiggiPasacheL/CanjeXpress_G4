// AuthProvider.js

import React, { createContext, useState, useEffect } from 'react';

export const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [authenticated, setAuthenticated] = useState(false);

  const login = (email, password) => {
    setLoading(true);

    // Implement your login logic here...

    return fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: email,
        password: password,
      }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          // Save the access token to localStorage
          localStorage.setItem('access_token', data.access_token);

          // Update the authenticated state
          setAuthenticated(true);

          setLoading(false);
          return data;
        } else {
          throw new Error(data.message || 'Login failed');
        }
      })
      .catch(error => {
        setLoading(false);
        console.error('Login error:', error.message);
        throw error;
      });
  };

  const createUser = (email, password) => {
    // Implementa tu lógica de creación de usuario aquí
    console.log('asdfasdf')
    };

    const signUpWithGmail = () => {
        // Implementa tu lógica de inicio de sesión con Google aquí
    };


    const logOut = () => {
        // Implementa tu lógica de cierre de sesión aquí
    };

    useEffect(() => {
        // Implementa tu lógica de verificación de sesión aquí
        // Actualiza el estado user y loading en consecuencia
    }, []);

  const authInfo = {
    user,
    loading,
    authenticated,
    createUser,
    login,
    logOut,
    signUpWithGmail,
  };

  return (
    <AuthContext.Provider value={authInfo}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;
