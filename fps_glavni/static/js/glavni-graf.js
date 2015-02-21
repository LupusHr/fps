//glavni graf

var chart = c3.generate({
	bindto: '#graph-container',
    data: {
    	x: "x",
        columns: party_columns,
        type: 'bar',
        names: {
            data1: 'Ukupni godišnji prihod',
        }
    },
    axis: {
        x: {
            type: 'category',
            tick: {
                rotate: 75,
                multiline: false
            },
            height: 130
        }
    }
});