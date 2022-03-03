install () {
	python3 -m pip install $1
}

install python-dotenv

# Install Python libraries for cloud provider
case $1 in
	"gcs")
		install google-cloud-storage 
		;;

	"azure")
		install azure-storage-blob 
		;;
	
	"aws")
		install boto3 
		;;
	
	*) ;;
esac

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
	cp .env.example .env
	sed -i "s/SERVICE_NAME=\"\"/SERVICE_NAME=\"$1\"" .env
fi