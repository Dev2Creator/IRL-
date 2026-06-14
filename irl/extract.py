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
import tarfile
import urllib.parse
from rich.progress import Progress, DownloadColumn, TransferSpeedColumn, TextColumn

def download_and_extract(url):
    print(f"\nDownloading from {url}...")
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        filename = "downloaded_package"
        cd = response.headers.get('content-disposition')
        if cd and 'filename=' in cd:
            filename = cd.split('filename=')[1].strip('"\'')
        else:
            parsed_url = urllib.parse.urlparse(url)
            base_name = os.path.basename(parsed_url.path)
            if base_name:
                filename = base_name
        
        with Progress(
            TextColumn("[bold blue]🌱 Touching grass..."),
            "[progress.percentage]{task.percentage:>3.0f}%",
            DownloadColumn(),
            TransferSpeedColumn()
        ) as progress:
            task = progress.add_task("Downloading", total=total_size)
            
            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        progress.update(task, advance=len(chunk))
                    
        extracted = False
        if zipfile.is_zipfile(filename):
            print("Extracting ZIP archive...")
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall(".")
            extracted = True
        elif tarfile.is_tarfile(filename):
            print("Extracting TAR archive...")
            with tarfile.open(filename, 'r:*') as tar_ref:
                tar_ref.extractall(".")
            extracted = True
            
        if extracted:
            os.remove(filename)
            
        print("✨ Successfully touched grass and installed the package!")
        
    except Exception as e:
        print(f"❌ Error during download/extraction: {e}")
