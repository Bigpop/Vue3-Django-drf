<template>

    <Header/>
    <WhisperList/>

</template>

<script>
    import Header from '@/components/Header.vue'
    import WhisperList from '@/components/whisper/WhisperList.vue'

    export default {
        name: 'Whisper',
        components: {Header, WhisperList}
    }
</script>