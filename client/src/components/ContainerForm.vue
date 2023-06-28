<template>
  <div class="container">
    <form>
      <div class="mb-3">
        <label class="">Container Name</label><br>
        <input
          v-model="name"
          type="text">
        <br><br>
        <div class="btn-group" role="group">
          <button
            type="button"
            class="btn btn-primary btn-sm"
            @click="addContainer">
            Submit
          </button>
          <button
            type="button"
            class="btn btn-danger btn-sm"
            @click="goBack">
            Cancel
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: "",
    };
  },
  methods: {
    addContainer() {
      const path = 'http://localhost:5001/new';
      const payload = {
        name: this.name,
      };
      axios.post(path, payload)
        .then((res) => {
          if(res.status === 200) {
            this.$router.push({ path: '/' });
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    goBack() {
      this.$router.push({ path: '/' });
    },
  },
};
</script>
