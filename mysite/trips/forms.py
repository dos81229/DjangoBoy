from django import forms

class MessageForm(forms.Form):
	留言者 	= forms.CharField(required = True)
	相片 	= forms.URLField(required = False)
	留言    = forms.CharField(required = True)
	出沒地點 = forms.CharField(required = False)
	喜歡的食物 = forms.CharField(required = False)
	好習慣   = forms.CharField(required = False)
	感情狀況 = forms.CharField(required = False)


class CommentForm(forms.Form):
    留言者    	 = forms.CharField(max_length=20)
    留言者信箱   = forms.EmailField(max_length=20, required=False)
    評論 		 = forms.CharField(max_length=200)

class MusicForm(forms.Form):
    留言者       = forms.CharField(max_length=20)
    留言者信箱   = forms.EmailField(max_length=20, required=False)
    評論         = forms.CharField(max_length=200)

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email 	  = forms.EmailField()
	message   = forms.CharField(widget=forms.Textarea)	

	def clean_full_name(self):
		cd = self.cleaned_data

		full_name = cd.get('full_name')

		if len(full_name) < 3:
			raise forms.ValidationError("請輸入兩個字以上!")

		return full_name

	def clean_message(self):
		cd = self.cleaned_data

		message = cd.get('message')

		if len(message) < 10 :
			raise forms.ValidationError("請輸入十個字以上!")

		return message 

	def clean(self):
		cd = self.cleaned_data

		email 	  = cd.get('email')
		full_name = cd.get('full_name')

		if email == full_name :
			raise forms.ValidationError("email should not be an full_name!")

		return cd 

		





