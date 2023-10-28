<template>
  <footer>
    <div class="container pt-5">
      <div class="row">
        <div class="col-md-3 col-6">
          <ul style="list-style-type: none">
            <li class="text-light font-weight-bold pb-2">Conocenos mejor</li>
            <li><a class="footer-link font-weight-light" href="#">Sobre nosotros</a></li>
            <li><a class="footer-link font-weight-light" href="#">Android App</a><br /></li>
            <li><a class="footer-link font-weight-light" href="#">iOS App</a><br /></li>
          </ul>
        </div>

        <div class="col-md-3 col-6">
          <ul style="list-style-type: none">
            <li class="text-light font-weight-bold">Contactanos</li>
            <li><a class="footer-link font-weight-light" href="#">Facebook</a></li>
            <li><a class="footer-link font-weight-light" href="#">Twitter</a><br /></li>
            <li><a class="footer-link font-weight-light" href="#">Instagram</a><br /></li>
          </ul>
        </div>

        <div class="col-md-3 col-6">
          <ul style="list-style-type: none">
            <li class="text-light font-weight-bold">Haz dinero con nosotros</li>
            <li><a class="footer-link font-weight-light" href="#">Vende con nosotros</a></li>
            <li>
              <a class="footer-link font-weight-light" href="#">Conviertete en proveedor</a><br />
            </li>
            <li>
              <a class="footer-link font-weight-light" href="#">Promociona tus productos</a><br />
            </li>
          </ul>
        </div>

        <div class="col-md-3 col-6">
          <ul style="list-style-type: none">
            <li class="text-light font-weight-bold">Dejanos ayudarte</li>
            <li><a class="footer-link font-weight-light" href="#">Devoluciones</a></li>
            <li><a class="footer-link font-weight-light" href="#">Ayuda</a><br /></li>
            <li>
              <a class="footer-link font-weight-light" href="#">Descarga nuestra app</a><br />
            </li>
          </ul>
        </div>
      </div>

      <div class="row">
        <div class="col-12">
          <div class="text-center py-5">
            <img id="logo" src="../assets/logo.png" />
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style>
footer {
  margin-top: 100px;
  background-color: #232f3e;
  font-size: 16px;
}

li {
  padding-left: 0;
  padding-bottom: 10px;
}

a {
  text-decoration: none;
}

.footer-link {
  color: #ddd;
}

#logo {
  width: 150px;
}

footer {
  font-family: 'Roboto', sans-serif;
}
</style>
