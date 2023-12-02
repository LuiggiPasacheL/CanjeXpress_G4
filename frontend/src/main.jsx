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
import Home from './pages/Home/Home.jsx';
import Shop from './pages/Shop/Shop.jsx';
import SingleProduct from './pages/Shop/SingleProduct.jsx';
import Blog from './pages/Blog/Blog.jsx';
import SingleBlog from './pages/Blog/SingleBlog.jsx';
import About from './pages/AboutPage/About.jsx';
import Contact from './pages/ContactPage/Contact.jsx';
import CartPage from './pages/Shop/CartPage.jsx';
import CheckoutPage from './pages/Shop/CheckoutPage.jsx';
import Signup from './components/Signup.jsx';
import Login from './components/Login.jsx';
import ErrorPage from './components/ErrorPage.jsx';
import PrivateRoute from './PrivateRoute/PrivateRoute.jsx';
import AuthProvider from './contexts/AuthProvider.jsx';

import BOHome from './pages/BackOffice/home/BOHome.jsx';
import UsersList from './pages/BackOffice/list/UsersList.jsx';
import ProductsList from './pages/BackOffice/list/ProductsList.jsx';
import CampaignsList from "./pages/BackOffice/list/CampaignsList.jsx";
import SingleUser from "./pages/BackOffice/single/SingleUser.jsx";
import BOSingleProduct from "./pages/BackOffice/single/BOSingleProduct.jsx";
import SingleCampaign from "./pages/BackOffice/single/SingleCampaign.jsx";
import NewUser from "./pages/BackOffice/new/NewUser.jsx";
import NewProduct from "./pages/BackOffice/new/NewProduct.jsx";
import NewCampaign from "./pages/BackOffice/new/NewCampaign.jsx";
import { productInputs, userInputs, campaignInputs } from "./utilis/formSource.js";


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
      {
        path: "/blog",
        element: <Blog/>
      },
      {
        path: "/blog/:id",
        element: <SingleBlog/>
      },
      {
        path: "/about",
        element: <About/>
      },
      {
        path: "/contact",
        element: <Contact/>
      },
      {
        path: "/cart-page",
        element: <CartPage/>
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
  {
    path: "/backoffice",
    element: <BOHome />,
  },
  {
    path: "/backoffice/users",
    element: <UsersList />
  },
  {
    path: "/backoffice/users/newUser",
    element: <NewUser
        title="Crear nuevo usuario"
    />
  },
  {
    path: "/backoffice/user/:userId",
    element: <SingleUser />
  },
  {
    path: "/backoffice/products",
    element: <ProductsList />
  },
  {
    path: "/backoffice/products/newProduct",
    element: <NewProduct
        title="Añadir nuevo producto"
    />
  },
  {
    path: "/backoffice/product/:productId",
    element: <BOSingleProduct />
  },
  {
    path: "/backoffice/campaigns",
    element: <CampaignsList />
  },
  {
    path: "/backoffice/campaigns/newCampaign",
    element: <NewCampaign
        title="Crear nueva campaña"
    />
  },
  {
    path: "/backoffice/campaign/:campaignId",
    element: <SingleCampaign />
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <AuthProvider>
     <RouterProvider router={router} />
  </AuthProvider>
  
)
