    #!/usr/bin/env python3
from datetime import datetime
from typing import List, Tuple
from uuid import uuid4
import base64
import io

from nicegui import Client, ui, events

# Add necessary imports for nicegui and other libraries


class File:
    def __init__(self, e: events.UploadEventArguments):
        self.name = e.name
        self.content = e.content.read()
        self.id = str(uuid4())
        self.uploaded_at = datetime.now()

    def showUploadedFile(self):
        with ui.expansion('show/hide uploded file').classes('w-full text-black'):
            base64_pdf = base64.b64encode(self.content).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="100%"></iframe>'
            ui.html(pdf_display).classes('w-full h-screen')

        # create a button to analyse the file

    def analyse(self,path):
        print(path)

with ui.column().classes("bg-gray-10 mx-auto my-auto"):
    with ui.row().classes("mx-auto my-auto"):
        ui.label('Resume Analyser').classes("font-bold text-2xl text-center")


with ui.row().classes("mx-auto my-auto"):
    # align links in a row
    file = ui.upload(
        label='Upload The Result Pdf File',
        on_upload=lambda e: File(e).showUploadedFile(),
        on_rejected=lambda e: ui.notify(f'Rejected {e}'),
        auto_upload=True
    ).props('accept=.pdf')
    
   
ui.run()
    

