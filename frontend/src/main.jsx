import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import 'swiper/css';

// bootstrap css
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';


// fonts and icons
import '././assets/css/icofont.min.css';
import '././assets/css/animate.css';
import '././assets/css/style.min.css';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Shop from './pages/Shop/Shop.jsx';
import SingleProduct from './pages/Shop/SingleProduct.jsx';
import CheckoutPage from './pages/Shop/CheckoutPage.jsx';
import Signup from './components/Signup.jsx';
import Login from './components/Login.jsx';
import ErrorPage from './components/ErrorPage.jsx';
import AuthProvider from './contexts/AuthProvider.jsx';


const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
    errorElement: <ErrorPage />,
    children:[
      {
        path: "/",
        element: <Shop/>
      },
      {
        path: "shop/:id",
        element: <SingleProduct/>
      },
    ]
  },
  {
    path: "/sign-up",
    element: <Signup/>
  },
  {
    path: "/login",
    element: <Login/>
  },
  {
    path: "/check-out",
    element: <CheckoutPage/>
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <AuthProvider>
     <RouterProvider router={router} />
  </AuthProvider>
  
)
