<template>
  <div class="home">
    <catalog />
  </div>
</template>

<script>
import Catalog from "@/components/Products/Catalog.vue";

export default {
  name: "home",
  components: {
    Catalog
  }
};
</script>
