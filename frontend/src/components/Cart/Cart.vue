<template>
  <section class="section columns">
    <div class="tile is-ancestor">
      <div class="tile is-parent is-vertical is-8">
        <article class="tile is-child notification">
          <p class="title">Shopping cart</p>
          <div class="card" v-for="product in cart" :key="product.id">
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img :src="product.image_url" />
                  </figure>
                </div>
                <div class="media-content">
                  <p class="title is-6">{{ product.name }}</p>
                  <p class="subtitle is-6">{{ product.type }}</p>
                  <p class="subtitle is-6">${{ product.price }}</p>
                  <star-rating
                    :rating="product.rating"
                    read-only
                    :show-rating="false"
                    :star-size="17"
                  />
                </div>
              </div>
            </div>
          </div>
        </article>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child notification">
          <div class="content">
            <p class="title">Subtotal</p>
            <p class="subtitle">With even more content</p>
            <div class="content">
              <!-- Content -->
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script>
import { HTTP } from "@/plugins/axios";

export default {
  data() {
    return {
      cart: {}
    };
  },
  async mounted() {
    await this.getCart();
  },
  methods: {
    async getCart() {
      return await HTTP.get(`/users/1/cart`).then(response => {
        return (this.cart = response.data.products);
      });
    }
  }
};
</script>

<style lang="sass" scoped>

</style>


