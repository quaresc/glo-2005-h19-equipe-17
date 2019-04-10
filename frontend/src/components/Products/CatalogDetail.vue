<template>
  <div class="column is-one-fifth-desktop is-two-thirds-tablet">
    <div class="card is-fullheight">
      <div class="card-image">
        <figure class="image is-square">
          <img :src="product.image_url" />
        </figure>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <p class="title is-6">{{ product.name }}</p>
            <p class="subtitle is-6">{{ product.type }}</p>
          </div>
        </div>
      </div>
      <footer class="card-footer">
        <div class="card-footer-item">${{ product.price }}</div>
        <div class="card-footer-item">
          <star-rating
            :rating="product.rating"
            read-only
            :show-rating="false"
            :star-size="17"
          />
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: Object
  }
};
</script>

<style lang="sass" scoped>
img
  object-fit: contain;
  cursor: pointer;
.card
  display: flex
  flex-direction: column
  &.is-fullheight
    height: 100%;
.card-footer
  margin-top: auto;
</style>