// Copyright (c) 2018, prafful and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article', {
	refresh: function(frm) {
		console.log('refreshing ... ', frm.doc.name);
	}
});
