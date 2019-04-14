<template>
  <section>
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
  </section>
</template>

<script>
export default {
  props: {
    cart: Array
  }
};
</script>

<style lang="sass" scoped>

</style>


