import React, { useState } from 'react'

import {
  Link
} from "react-router-dom"

import logo from "../assets/images/logo/logo.png"

export const NavItems = () => {

  const [menuToggle, setMenuToggle] = useState(false)
  const [socialToggle, setSocialToggle] = useState(false)
  const [headerFixed, setHeaderFixed] = useState(false)

  window.addEventListener("scroll", () => {
    if(window.scrollY > 200) setHeaderFixed(true)
    else setHeaderFixed(false)
  })

  return (
    <header className={`header-section style-4 ${headerFixed ? "header-fixed fadeInUp" : ""}`}>
      <div className={`header-top d-md-none ${socialToggle ? "open": ""}`}>
        <div className='container'>
          <div className='header-top-area'>
            <Link to="signup" className="lab-btn me-3"><span>Registrate</span></Link>
            <Link to="/login">Iniciar Sesion</Link>
          </div>
        </div>
      </div>
      <div className='header-bottom'>
        <div className='container'>
          <div className='header-wrapper'>
            {/* Logo */}
            <div className='logo'>
              <Link to={"/"}>
                <img src={logo} alt="" />
              </Link>
            </div>
            {/* Area de menu */}
            <div className='menu-area'>
              <div className="menu">
                <ul className={`lab-ul ${menuToggle ? "active" : ""}`}>
                  <li><Link to="/">Home</Link></li>
                  <li><Link to="/shop">Tienda</Link></li>
                  <li><Link to="/blog">Blog</Link></li>
                  <li><Link to="/about">Nosotros</Link></li>
                  <li><Link to="/contact">Contactanos</Link></li>
                </ul>
              </div>
              <Link
                to="/sign-up"
                className='lab-btn me-3 d-none d-md-block'
              >
                Registrate
              </Link>
              <Link
                to="/login"
                className='d-none d-md-block'
              >
                Inicia Sesion
              </Link>
              {/* Menu Toggler */}
              <div onClick={() => setMenuToggle(!menuToggle)} className={`header-bar d-lg-none ${menuToggle ? "active" : ""}`}>
                <span></span>
                <span></span>
                <span></span>
              </div>

              {/* Social Toggler */}
              <div
                className='ellepsis-bar d-md-none'
                onClick={() => setSocialToggle(!socialToggle)}
              >
                <i className='icofont-info-square'></i>

              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  )
}