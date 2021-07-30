# INSTALL
1. Use **Python 3.7**.
2. Install package:
   ```
   pip install https://github.com/AcademySoftwareFoundation/OpenCue/releases/download/v0.8.8/pycue-0.8.8-all.tar.gz
   pip install https://github.com/AcademySoftwareFoundation/OpenCue/releases/download/v0.8.8/pyoutline-0.8.8-all.tar.gz
   pip install https://github.com/AcademySoftwareFoundation/OpenCue/releases/download/v0.8.8/cueadmin-0.8.8-all.tar.gz
   pip install https://github.com/AcademySoftwareFoundation/OpenCue/releases/download/v0.8.8/cuegui-0.8.8-all.tar.gz
   pip install https://github.com/AcademySoftwareFoundation/OpenCue/releases/download/v0.8.8/cuesubmit-0.8.8-all.tar.gz
   ```
3. Set environment variables:

   ```
   CUEBOT_HOSTS=CUBOT_IP_OR_HOSTNAME
   OL_CONFIG=path\to\outline.cfg
   ```

# EXECUTE
```shell
cueadmin  # Command line manager
cuegui  # GUI for monitoring
cuesubmit  # Submit job, not works well
python pycuerun  # "Python" need to be added in Windows 
```

# FIX
File `PYTHONPATH/bin/cuerunbase.py` line `139`:
```python
        except ValueError:
```
Should changes to:
```python
        except (ValueError, AttributeError):
```