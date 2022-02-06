<template>
    <div>
        <footer>
            <p>
                Made with &#10084; by <a href='https://tejas-gosavi.github.io/'>Tejas Gosavi</a>
            </p>
        </footer>
    </div>
</template>

<script>
export default {
    name: "Footer",
};
</script>

<style scoped>
footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
    font-size: 20px;
}
a {
    font-weight: bold;
    text-decoration: none;
    color: #2c3e50;
}
</style>