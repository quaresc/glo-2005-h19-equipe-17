<template>
  <section class="section">
    <div class="tile">
      <div class="tile is-child box notification">
        <div class="content">
          <form @submit="sumbitReview">
            <b-field label="Title">
              <b-input v-model="title" type="text" maxlength="45"></b-input>
            </b-field>
            <b-field label="Rating">
              <star-rating
                :rating="1"
                :show-rating="false"
                :star-size="20"
                @rating-selected="setRating"
              />
            </b-field>
            <b-field label="Comment">
              <b-input
                v-model="comment"
                type="textarea"
                maxlength="1000"
              ></b-input>
            </b-field>
            <button class="button is-primary is-rounded" type="submit">
              Sumbit
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { HTTP } from "@/plugins/axios";

export default {
  data() {
    return {
      review: null,
      title: null,
      rating: 5,
      comment: null
    };
  },
  async mounted() {},
  methods: {
    setRating: function(rating) {
      this.rating = rating;
    },
    fieldsFilled() {
      if (!this.title) {
        this.$toast.open({
          message: "Please insert a title.",
          position: "is-bottom",
          type: "is-danger"
        });
        return false;
      } else if (!this.comment) {
        this.$toast.open({
          message: "Please insert a comment.",
          position: "is-bottom",
          type: "is-danger"
        });
        return false;
      } else {
        return true;
      }
    },
    async sumbitReview() {
      if (this.fieldsFilled()) {
        const review = {
          title: this.title,
          comment: this.comment,
          rating: this.rating
        };
        let productId = this.$route.params.id;
        let userId = 1; // TODO: Replace with a real variable
        try {
          await HTTP.put("/products/" + productId + "/reviews/" + userId, {
            review
          }).then(response => {
            if (response.data === "Duplicate") {
              this.$toast.open({
                duration: 5000,
                message: "You already added a review for this product.",
                position: "is-bottom",
                type: "is-danger"
              });
            } else {
              this.$toast.open({
                message: "Thank you for your review!",
                type: "is-success"
              });
              this.$router.go();
            }
          });
        } catch (error) {
          console.error(error);
        }
      }
    }
  }
};
</script>
