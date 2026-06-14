# IRL™ 🌱 - Software for Humans
# Copyright (C) 2026 UNKNOWN™
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import requests
import zipfile
from rich.progress import Progress, DownloadColumn, TransferSpeedColumn, TextColumn

def download_and_extract(url):
    print(f"\nDownloading from {url}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        zip_path = "temp_download.zip"
        
        with Progress(
            TextColumn("[bold blue]🌱 Touching grass..."),
            "[progress.percentage]{task.percentage:>3.0f}%",
            DownloadColumn(),
            TransferSpeedColumn()
        ) as progress:
            task = progress.add_task("Downloading", total=total_size)
            
            with open(zip_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
                    progress.update(task, advance=len(chunk))
                    
        print("Extracting files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")
            
        os.remove(zip_path)
        print("✨ Successfully touched grass and installed the package!")
        
    except Exception as e:
        print(f"❌ Error during download/extraction: {e}")
