<template>
  <div class="columns is-centered">
    <div class="column has-text-centered">
      <p class="title is-1">Oops ! Page not found !</p>
      <p class="subtitle is-3">
        We can't seem to find the page you're looking for.
      </p>
      <router-link :to="{ name: 'Home' }">
        <a class="button is-primary is-large">Back to home</a>
      </router-link>
    </div>
  </div>
</template>
