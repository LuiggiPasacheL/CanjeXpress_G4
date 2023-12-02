import React, { useEffect } from "react";
import { Component, Fragment, useState } from "react";
import Pagination from "./Pagination";
import ProductCards from "./ProductCards";
const showResult = "Mostrando productos...";
import Data from "/src/products.json"

// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getAnalytics } from 'firebase/analytics';
import { getFirestore, collection, getDocs } from 'firebase/firestore';

const Shop = () => {

  // Your web app's Firebase configuration
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

  const [GridList, setGridList] = useState(true);
  const [products, setProducts] = useState([]);

  // pagination
  // Get current products to display
  const [currentPage, setCurrentPage] = useState(1);
  const productsPerPage = 12; // Number of products per page

  const indexOfLastProduct = currentPage * productsPerPage;
  const indexOfFirstProduct = indexOfLastProduct - productsPerPage;
  const currentProducts = products.slice(indexOfFirstProduct,indexOfLastProduct);

  // Function to change the current page
  const paginate = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  useEffect(() => {       
    // Fetch products and campaigns from Firestore when the component mounts
    const fetchData = async () => {
      try {
        const db = getFirestore(app);
        const productosRef = collection(db, 'productos');
        const campanasRef = collection(db, 'campañas');
        const productosSnapshot = await getDocs(productosRef);
        const campanasSnapshot = await getDocs(campanasRef);
        const fechaActual = new Date();
  
        const campanasMap = campanasSnapshot.docs.reduce((acc, doc) => {
          const data = doc.data();
          acc[data.id] = data;
          return acc;
        }, {});
  
        const firestoreProducts = productosSnapshot.docs.map((doc) => {
          const producto = doc.data();
          const campana = campanasMap[producto.campana_id];
          
          if (campana) {
            const fechaFinCampana = new Date(campana.end_date);
            console.log("HAY CAMPANIA")
            if (fechaFinCampana > fechaActual) {
              console.log("SI ES VIGENTE")

              return {
                ...producto,
                descuento: campana.discount,
                fecha_inicio: campana.start_date,
                fecha_fin: campana.end_date,
              };
            }
          }
          console.log("NO VIGENTE")
          return producto;
        });
  
        setProducts(firestoreProducts);
      } catch (error) {
        console.error('Error fetching Firestore data:', error);
      }
    };
  
    fetchData();
  }, [app]);
  
  

  return (
    <div>
      {/* shop page */}
      <div className="shop-page padding-tb">
        <div className="container">
          <div className="row justify-content-center">
            <div className="col-lg-12 col-12">
              <article>
                <div className="shop-title d-flex flex-wrap justify-content-between">
                  <p>{showResult}</p>
                  <div
                    className={`product-view-mode ${
                      GridList ? "gridActive" : "listActive"
                    }`}
                  >
                    <a className="grid" onClick={() => setGridList(!GridList)}>
                      <i className="icofont-ghost"></i>
                    </a>
                    <a className="list" onClick={() => setGridList(!GridList)}>
                      <i className="icofont-listine-dots"></i>
                    </a>
                  </div>
                </div>
                <div>
                  <ProductCards
                    products={currentProducts}
                    GridList={GridList}
                  />
                </div>
                <Pagination
                  productsPerPage={productsPerPage}
                  totalProducts={products.length}
                  paginate={paginate}
                  activePage={currentPage}
                />
              </article>
            </div>
            <div className="col-lg-4 col-12">
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Shop;
