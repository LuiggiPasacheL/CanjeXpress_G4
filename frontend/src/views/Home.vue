<template>
  <div id="home">
    <div id="background-div" class="page-holder bg-cover">
      <div class="container py-5">
        <header class="text-left text-white py-5">
          <h3 class="mb-4 rounded">
            <a class="bg-white px-2 py-2 rounded" id="heading">Bienvenido a CanjeXpress</a>
          </h3>
          <p id="content" class="lead mb-0 bg-dark p-1 rounded">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit magnam non dolore? Modi
            eveniet beatae rerum! Ut placeat, odio sapiente ad sequi saepe optio voluptatum quam
            sit, assumenda animi sunt.
          </p>
        </header>
      </div>
    </div>

    <div class="container py-2">
      <div class="row">
        <div class="col-12 text-left">
          <h2 class="pt-3">Productos destacados</h2>
        </div>
      </div>
      <div class="row">
        <div
          v-for="index in this.product_size"
          :key="index"
          class="col-md-6 col-xl-4 col-12 pt-3 justify-content-around d-flex"
        >
          <ProductBox :product="products[index - 1]" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProductBox from '../components/ProductBox.vue'

export default {
  components: {
    ProductBox
  },
  props: ['products'],
  data() {
    return {
      product_size: 0
    }
  },
  mounted() {
    this.product_size = Math.min(8, this.products.length)
  }
}
</script>

<style>
.page-holder {
  min-height: 100vh;
}

.bg-cover {
  background-size: cover !important;
}

#background-div {
  background: url(../assets/home.jpeg);
}

#heading {
  text-decoration: none;
  font-family: 'Roboto', sans-serif;
  font-weight: 400;
  opacity: 0.8;
  font-family: 'Josefin Sans', sans-serif;
}

#content {
  opacity: 0.8;
}

h2 {
  font-family: 'Josefin Sans', sans-serif;
}
</style>
