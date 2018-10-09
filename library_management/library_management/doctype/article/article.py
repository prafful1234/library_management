# -*- coding: utf-8 -*-
# Copyright (c) 2018, prafful and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Article(Document):
	def validate(self):
		if self.author == 'ABC':
			frappe.throw('author ABC not allowed')

