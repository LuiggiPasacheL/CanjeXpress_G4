import Sidebar from "../../../components/Backoffice/sidebar/Sidebar";
import Navbar from "../../../components/Backoffice/navbar/Navbar";
import "./home.scss";
import Widget from "../../../components/Backoffice/widget/Widget";
import Table from "../../../components/Backoffice/table/Table";

import { useContext, useEffect } from 'react';
import { AuthContext } from '../../../contexts/AuthProvider';


const BOHome = () => {
  const { authenticated, login, logOut } = useContext(AuthContext);

  const existingToken = localStorage.getItem('access_token');

  useEffect(() => {
      if (existingToken && !authenticated) {
        login("user1", "password123")
          .then((result) => {
            // Signed in
            const user = result;
            console.log(user);
            // ...
          })
          .catch((error) => {
            const errorMessage = error.message;
            setErrorMessage("Please provide valid email & password!");
          });
      } else {
        console.log('token de acceso en el almacenamiento local');
      }
  });
  
  return (
    <div className="home">
      <Sidebar />
      <div className="homeContainer">
        <Navbar />
        <div className="widgets">
          <Widget type="user" />
          <Widget type="order" />
          <Widget type="earning" />
          <Widget type="balance" />
        </div>
        <div className="listContainer">
          <div className="listTitle">Ultimas Transacciones</div>
          <Table />
        </div>
      </div>
    </div>
  );
};

export default BOHome;
