import os
import shutil

def main():
    os.system("python manage.py collectstatic")
    os.makedirs('tmp', exist_ok=True)
    os.system("python manage.py distill-local tmp")

    for file in os.listdir('tmp'):
        distill_path = os.path.join('distill', file)
        tmp_path = os.path.join('tmp', file)
        
        # 删除distill下同名文件或目录
        if os.path.exists(distill_path):
            if os.path.isdir(distill_path):
                shutil.rmtree(distill_path)
            else:
                os.remove(distill_path)

        # 移动tmp文件到distill
        os.rename(tmp_path, distill_path)

    os.rmdir('tmp')

if __name__ == "__main__":
    main()