<template>
  <div class="container">
    <form>
      <div class="mb-3">
        <label>Container Name</label><br>
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
      const path = '/api/containers/new';
      const payload = {
        name: this.name,
      };
      axios.post(path, payload)
        .then((res) => {
          if(res.status === 200) {
            this.$emit('showContainerList', true);
            this.$emit('showContainerNewForm', false);
            this.$parent.handleMessage('Container created!');
            this.$parent.getContainers();
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    goBack() {
      this.$emit('showContainerList', true);
      this.$emit('showContainerNewForm', false);
    },
  },
};
</script>
