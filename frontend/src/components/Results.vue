<template>
	<div>
        <p><b>{{ text }}</b></p>
        <p>Predicted Category - {{ Object.keys(result)[0] }}</p>
		<table>
            <thead>
                <tr>
                    <th>Category</th>
                    <th>Probability</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(p, c) in result" :key="c">
                    <td>{{ c }}</td>
                    <td>{{ p }}</td>
                </tr>
            </tbody>
		</table>
	</div>
</template>

<script>
export default {
	name: "Results",
    props: {"text": String, "result": Object},
};
</script>

<style scoped>
p {
    text-align: center;
}

table, td, th {
	border: 1px solid #ddd;
	text-align: left;
}

table {
    margin: auto;
	border-collapse: collapse;
	width: 30%;
}

th, td {
	padding: 15px;
}

</style>