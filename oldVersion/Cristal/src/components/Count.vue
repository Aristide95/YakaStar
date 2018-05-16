<template>
  <div class="iCountUp">
    <ICountUp
      :startVal="startVal"
      :endVal="endVal"
      :decimals="decimals"
      :duration="duration"
      :options="options"
      @ready="onReady"
    />
  </div>
</template>

<script type="text/babel">
import ICountUp from 'vue-countup-v2'
export default {
  name: 'Counter',
  components: {
    ICountUp
  },
  props: ['end'],
  data () {
    return {
      startVal: 0,
      endVal: this.end,
      decimals: 0,
      duration: 4,
      options: {
        separator: '',
        decimal: '.'
      }
    }
  },
  methods: {
    onReady: function (instance) {
      const that = this
      instance.update(that.endVal)
    }
  }
}
</script>

<style scoped>
  .iCountUp {
    text-align: center;
    font-size: 60px;
    color: #0c365a;
  }
</style>
