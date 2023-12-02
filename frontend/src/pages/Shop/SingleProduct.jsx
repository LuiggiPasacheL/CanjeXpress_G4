import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import PageHeader from "../../components/PageHeader";
import PopularPost from "./PopularPost";
import Tags from "./Tags";
import Rating from "../../components/Sidebar/rating";

import { Swiper, SwiperSlide } from "swiper/react";
// Import Swiper styles
import "swiper/css";

// import required modules
import { Autoplay } from "swiper/modules";
import Review from "../../components/Review";
import MostPopularPost from "../../components/Sidebar/MostPopularPost";
import ProductDisplay from "./ProductDisplay";
const reviwtitle = "Add a Review";

// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getAnalytics } from 'firebase/analytics';
import { getFirestore, collection, getDocs, query, where } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyBs_9dsYiDN16wGw8Tm3EwqperjpUxY--M",
  authDomain: "g5-arquitectura.firebaseapp.com",
  projectId: "g5-arquitectura",
  storageBucket: "g5-arquitectura.appspot.com",
  messagingSenderId: "734139387824",
  appId: "1:734139387824:web:7dba57e18a3447f24ad075",
  measurementId: "G-707LK21PSY"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const SingleProduct = () => {
  const [product, setProduct] = useState([]);
  const { id } = useParams();



  useEffect(() => {
    const fetchData = async () => {
      const db = getFirestore(app);
      const productosRef = collection(db, 'productos');
      const querySnapshot = await getDocs(productosRef);
      const firestoreProducts = querySnapshot.docs.map((doc) => doc.data());
      const productFilter = firestoreProducts.filter((product) => product.id === parseInt(id));
      console.log(productFilter)
      setProduct(productFilter);
    };
    fetchData();
  }, [id, db]);

  return (
    
    <div>
      <div className="shop-single padding-tb aside-bg">
        <div className="container">
          <div className="row justify-content-center">
            <div className="col-lg-12 col-12">
              <article>
              <div className="product-details">
                  <div className="row align-items-center">
                    <div className="col-md-6 col-12">
                      <div className="product-thumb">
                        <div className="swiper-container pro-single-top">
                          <Swiper
                            spaceBetween={30}
                            slidesPerView={1}
                            loop={"true"}
                            autoplay={{
                              delay: 2000,
                              disableOnInteraction: false,
                            }}
                            modules={[Autoplay]}
                            navigation={{
                              prevEl: ".pro-single-prev",
                              nextEl: ".pro-single-next",
                            }}
                          >
                            {product.map((item, i) => (
                              <SwiperSlide key={i}>
                                <div className="single-thumb">
                                  <img src={item.image} alt="" />
                                </div>
                              </SwiperSlide>
                            ))}
                          </Swiper>
                          <div className="pro-single-next">
                            <i className="icofont-rounded-left"></i>
                          </div>
                          <div className="pro-single-prev">
                            <i className="icofont-rounded-right"></i>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div className="col-md-6 col-12">
                      <div className="post-content">
                        <div>
                          {
                            product.map(item => <ProductDisplay item={item} key={item.id}/>)
                          }
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                
              </article>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SingleProduct;
