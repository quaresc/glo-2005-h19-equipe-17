<template>
  <div>
    <ul>
      <li v-for="user in users" :key="user.id">
        {{ user.first_name }}
        {{ user.last_name }}
        {{ user.age }}
      </li>
    </ul>
  </div>
</template>

<script>
import { HTTP } from "@/plugins/axios";

export default {
  name: "Users",
  props: {
    msg: String
  },
  data() {
    return {
      users: null
    };
  },
  async mounted() {
    try {
      this.users = await HTTP.get("/users").then(response => {
        return response.data;
      });
    } catch (error) {
      console.error(error);
    }
  }
};
</script>

<style scoped></style>
