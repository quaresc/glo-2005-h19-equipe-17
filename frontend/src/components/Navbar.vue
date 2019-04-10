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

          <div class="navbar-dropdown" v-if="departments">
            <a
              class="navbar-item"
              v-for="(department, index) in departments"
              :key="index"
              @click="redirect(department.name)"
              >{{ department.name }}</a
            >
            <hr class="navbar-divider" />
            <a
              class="navbar-item"
              @click="
                router.push({
                  name: 'Catalog'
                })
              "
            >
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
import { HTTP } from "@/plugins/axios";
export default {
  data() {
    return {
      departments: null
    };
  },
  async mounted() {
    this.getDepartements();
  },
  methods: {
    async getDepartements() {
      try {
        await HTTP.get("/departments/").then(response => {
          this.departments = response.data.departments;
        });
      } catch (error) {
        console.error(error);
      }
    },
    redirect(department) {
      this.$router.push({
        name: "Catalog",
        params: { department: department }
      });
    }
  }
};
</script>

<style scoped>
</style>
