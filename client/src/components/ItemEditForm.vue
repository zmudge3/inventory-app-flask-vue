<template>
  <div class="container">
    <form>
      <div class="mb-3">
        <label>Name</label><br>
        <input
          v-model="itemForEdit.name"
          type="text">
        <br>
        <label>Quantity</label><br>
        <input
          v-model="itemForEdit.quantity"
          type="text">
        <br><br>
        <div class="btn-group" role="group">
          <button
            type="button"
            class="btn btn-primary btn-sm"
            @click="editItem">
            Save
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
  props: ['itemForEdit'],
  methods: {
    editItem() {
      const path = `/api/items/${this.itemForEdit.id}`;
      const payload = {
        name: this.itemForEdit.name,
        quantity: this.itemForEdit.quantity,
      };
      axios.put(path, payload)
        .then((res) => {
          if(res.status === 200) {
            this.$emit('showContainerItems', true);
            this.$emit('showItemEditForm', false);
            this.$parent.handleMessage('Item updated');
            this.$parent.getItems();
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    goBack() {
      this.$emit('showContainerItems', true);
      this.$emit('showItemEditForm', false);
    },
  },
};
</script>
