<template>
  <nav
    class="navbar is-fixed-top"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="navbar-brand">
      <a class="navbar-item">
        <router-link :to="{ name: 'Home' }">
          <div class="is-size-2-desktop is-size-2-touch">
            <a>WorstBuy</a>
          </div>
        </router-link>
      </a>

      <a
        role="button"
        class="navbar-burger burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item">
          Home
        </a>

        <a class="navbar-item">
          About us
        </a>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            Departments
          </a>

          <div class="navbar-dropdown">
            <a class="navbar-item">
              Electronics
            </a>
            <a class="navbar-item">
              Computers
            </a>
            <a class="navbar-item">
              Beauty & Personal Care
            </a>
            <hr class="navbar-divider" />
            <a class="navbar-item">
              Check all products
            </a>
          </div>
        </div>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a class="button is-primary">
              <strong>Sign up</strong>
            </a>
            <a class="button is-light">
              Log in
            </a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {};
</script>

<style scoped>
</style>
