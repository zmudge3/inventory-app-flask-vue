<template>
  <div class="container">
    <form>
      <div class="mb-3">
        <label>Item Name</label><br>
        <input
          v-model="name"
          type="text">
        <br><br>
        <div class="btn-group" role="group">
          <button
            type="button"
            class="btn btn-primary btn-sm"
            @click="addItem">
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
  props: ['containerID'],
  methods: {
    addItem() {
      const path = `http://localhost:5001/containers/${this.containerID}/new_item`;
      const payload = {
        name: this.name,
      };
      axios.post(path, payload)
        .then((res) => {
          if(res.status === 200) {
            this.$emit('showContainerItems', true);
            this.$emit('showItemForm', false);
            this.$parent.handleMessage('Item created!');
            this.$parent.getItems();
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    goBack() {
      this.$emit('showContainerItems', true);
      this.$emit('showItemForm', false);
    },
  },
};
</script>
