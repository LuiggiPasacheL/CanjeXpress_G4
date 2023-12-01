// AuthProvider.js

import React, { createContext, useState, useEffect } from 'react';
import PropTypes from 'prop-types';
export const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [authenticated, setAuthenticated] = useState(false);
  const loginApiUrl = 'http://34.125.166.120/api/login/login'
  const userDataApiUrl = 'http://34.125.166.120/api/login/user-data'
  
  const login = (email, password) => {
    setLoading(true);

    // Implement your login logic here...

    return fetch(loginApiUrl, {
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
          console.log(data.access_token)
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

  const user_data = () => {
    console.log('user_data');
    const accessToken = localStorage.getItem('access_token');
  
    if (accessToken === null) {
      console.warn('Access token not found. Returning null.');
      return Promise.resolve(null);
    }
  
    setLoading(true);
  
    return fetch(userDataApiUrl, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          // Update the authenticated state
          setAuthenticated(true);
          setLoading(false);
          return data.data; // Return only the 'data' field
        } else {
          throw new Error(data.message || 'Failed to fetch user data');
        }
      })
      .catch(error => {
        setLoading(false);
        console.error('User data fetch error:', error.message);
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
      console.log('asdfasdf')
      console.log(localStorage.getItem('access_token'))
      // Set the access token to null in localStorage
      localStorage.clear();
      
      console.log(localStorage.getItem('access_token'))
      // Update the authenticated state
      setAuthenticated(false);
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
    user_data,
  };

  return (
    <AuthContext.Provider value={authInfo}>
      {children}
    </AuthContext.Provider>
  );
};

AuthProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

export default AuthProvider;