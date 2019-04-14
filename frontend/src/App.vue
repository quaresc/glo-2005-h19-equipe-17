<template>
  <div id="app">
    <navbar></navbar>
    <router-view :key="$route.fullPath" />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar/Navbar.vue";

export default {
  components: {
    Navbar
  }
};
</script>


<style lang="scss">
// Import Bulma's core
@import "~bulma/sass/utilities/_all";

// Set your colors
$primary: #fcbd69;
$primary-invert: findColorInvert($primary);
$secondary: #222f3e;
$secondary-invert: findColorInvert($secondary);

// Setup $colors to use as bulma classes (e.g. 'is-secondary')
$colors: (
  "white": (
    $white,
    $black
  ),
  "black": (
    $black,
    $white
  ),
  "light": (
    $light,
    $light-invert
  ),
  "dark": (
    $dark,
    $dark-invert
  ),
  "primary": (
    $primary,
    $primary-invert
  ),
  "info": (
    $info,
    $info-invert
  ),
  "success": (
    $success,
    $success-invert
  ),
  "warning": (
    $warning,
    $warning-invert
  ),
  "danger": (
    $danger,
    $danger-invert
  ),
  "secondary": (
    $secondary,
    $secondary-invert
  )
);

// Links
$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
