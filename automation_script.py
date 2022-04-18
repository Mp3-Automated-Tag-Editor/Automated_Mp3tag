# Import pywinauto Application class
from pywinauto.application import Application
# Start a new process and specify a path to the text file
app = Application().start('notepad.exe', timeout=10) 

# Connect to already running process:
# By PID
app = Application(backend="uia").connect(process=1234)
  
# By path to executable
app = Application(backend="uia").connect(path=r"C:\Windows\System32\Notepad.exe")
  
# By regular expression
app = Application(backend="uia").connect(title_re=".*Notepad*") 

# Main window specification
main_dlg = app.UntitledNotepad
main_dlg.wait('visible') 

main_dlg = app.window(title='Untitled - Notepad') 

# Print all controls on the dialog
main_dlg.print_control_identifiers() 

main_dlg.Edit.type_keys("Hello pywinauto!\n\t It’s a sample text^A",
                        with_spaces=True,
                        with_newlines=True,
                        pause=0.5,
                        with_tabs=True) 

font_menu = main_dlg.menu_select('Format->Font...')
font_dlg = app.Font
font_type = font_dlg.ComboBox
font_type.select('Comic Sans MS')
font_style = font_dlg.ComboBox2
font_style.select('Bold')
font_size = font_dlg.ComboBox3
font_size.type_keys('18')
font_dlg.OK.click() 

# Select Print menu item. Wait for the dialog to appear
print_menu_item = main_dlg.menu_select('File->Print...')
print_dlg = app.Print
print_dlg.wait('ready')
  
# Select PDF printer
button = print_dlg.GroupBox
button.set_focus()
syslistview = print_dlg.ListView
listview_item = syslistview.get_item('Microsoft Print to PDF')
listview_item.click() 

# Open print preference
preference = print_dlg.Preferences.click()
print_pref_dlg = app.window(title='Printing Preferences')
print_pref_dlg.wait('ready')
# Set landscape
print_pref_dlg.ComboBox.select('Landscape')
#Open advanced settings
print_pref_dlg['Advanced...'].click()
adv_dlg = app.window(title='Microsoft Print To PDF Advanced Options')
adv_dlg.wait('ready')
# Select A3 size and save
paper_size = adv_dlg['2', 'ComboBox']
paper_size.select('A3')
  
adv_dlg.OK.click()
print_pref_dlg.OK.click()
print_dlg.Print.click() 

# Save the file
save_dlg = app.window(title='Save Print Output As')
save_dlg.wait('ready')
file_path = 'C:\Test\txt_to_pdf.pdf'
file_name_field = save_dlg['5']
file_name_field.type_keys(file_path)
save_dlg.Save.click()
# Clear the text and close Notepad
main_dlg.Edit.type_keys(u'{DELETE}')
main_dlg.close() 