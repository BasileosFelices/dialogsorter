#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;


std::string squeezeSpace (const std::string & text) {
    std::string result;
    auto readIterator = text.begin();
    bool prevSpace = false;
    for(;readIterator != text.end(); readIterator++) {
        if ( (*readIterator) == ' ') {
            if ( !prevSpace ) {
                prevSpace = true;
                result.push_back(*readIterator);
                continue;
            }

        }
        else{
            prevSpace = false;
            result.push_back(*readIterator);
        }

    }

    return result;
}

std::string trimLeftSpace (const std::string & text)  {
    size_t start = text.find_first_not_of(" ");
    return (start == std::string::npos) ? "" : text.substr(start);
}

std::string trimRightSpace (const std::string & text)  {
    size_t end = text.find_last_not_of(" ");
    return (end == std::string::npos) ? "" : text.substr(0, end + 1);
}
std::string trimSpace (const std::string & text)  {
    return trimLeftSpace ( trimRightSpace( text ) );
}


std::string cleanSpace (const std::string & text) {
    return squeezeSpace( trimSpace( text ));
}

int convertToNumber(const std::string & textnumber) {
    int number;
    try {
        number = std::stoi( cleanSpace(textnumber) );
    }
    catch (...)
    {
        return -1;
    }
    return number;
}

std::string readConsoleLine () {

    std::string consoleLine;

    std::getline(std::cin, consoleLine);

    return consoleLine;
}

std::string readFileLine (ifstream & file) {

    std::string line;

    std::getline(file, line);

    return line;
}

class Person {
private:
public:
    std::string mEmail;
    std::string mName;
    std::string mSurname;
    std::string mClass;

    std::vector<std::string> mPreferences;

    Person(const string & email, const string & name, const string & surname, const string & classname, const std::vector<std::string> & preferences) 
        : mEmail(email), mName(name), mSurname(surname), mClass(classname), mPreferences(preferences) {}

    void print() const {
        cout << mEmail << mName << mSurname << mClass << endl;
        for (auto pref : mPreferences) {
            cout << "<" << pref << "> ";
        }
        cout << endl;
    }

    bool operator < (const Person & other) const {
        return mEmail < other.mEmail;
    }

    friend ostream & operator << (ostream & os, const Person & p) {
        return os << p.mEmail << ";" << p.mName << ";" << p.mSurname << ";" << p.mClass << ";";
    }
};

class Activity {
private:
public:
    std::string mName;
    std::vector<Person> mAtendees;
    int mCapacity;
    int mOccupancy;

    Activity(const std::string & name, int cap) 
        : mName(name), mCapacity(cap), mOccupancy(0) {}
    
    Activity(const std::string & name) 
        : mName(name), mCapacity(0), mOccupancy(0) {}

    bool operator < (const Activity & other) const {
        return mName < other.mName;
    }

    bool addPerson (const Person & newperson) {
        if (mOccupancy < mCapacity) {
            // cerr << newperson << endl;
            mAtendees.push_back(newperson);
            mOccupancy++;
            return true;
        }
        return false;
    }

    friend ostream & operator << (ostream & os, const Activity & a) {
        return os << "Activity '" << a.mName << "' has capacity " << a.mCapacity << " filled to " << a.mOccupancy;
    }

};

class Sorter {
private:
    std::queue<Person> mAskers;
    std::map<string, Activity> mActivities;
public:

    void readData () {

        cout << "Please data file name: " << endl;
        string dataFileName = readConsoleLine();

        string dataFilePath = dataFileName;
        dataFilePath.append(".csv");

        ifstream dataFile (dataFilePath);
        if ( ! dataFile.is_open() ) {
            throw invalid_argument("Unable to open datafile");
        }

        while (! dataFile.eof()) {
            processDataLine( readFileLine(dataFile) );
        }

        string blokInfoFilePath = dataFileName;
        blokInfoFilePath.append("Info.csv");

        ifstream blokFile (blokInfoFilePath);
        if ( ! blokFile.is_open() ) {
            throw invalid_argument("Unable to open blokFile");
        }
        while (! blokFile.eof()) {
            processBlokFileLine( readFileLine(blokFile) );
        }

    }

    bool processDataLine(const std::string & dataLine) {
        if (dataLine.empty()) {
            return false;
        }

        std::istringstream line (dataLine); 
        std::string token;
        // dump time info
        std::getline(line, token, ';');

        // email
        std::getline(line, token, ';');
        std::string email = cleanSpace(token);

        // name
        std::getline(line, token, ';');
        std::string name = cleanSpace(token);
        // surname
        std::getline(line, token, ';');
        std::string surname = cleanSpace(token);
        // class
        std::getline(line, token, ';');
        std::string classnumber = cleanSpace(token);
        // preferences
        std::vector<std::string> preferences;
        while (!line.eof()) {
            std::getline(line, token, ';');
            cout << "|" << token << "|" << token << "|" << endl;
            preferences.push_back( cleanSpace(token) );
        }

        mAskers.push( Person(email, name, surname, classnumber, preferences) );

        // debugprint
        // cout << email << name << surname << classnumber << endl;
        // for (auto pref : preferences) {
        //     cout << pref;
        // }
        // cout << endl;

        return true;
    }

    bool processBlokFileLine (const std::string & blokline) {
        // cerr << blokline << endl;
        if(blokline == "") {
            return false;
        }

        std::istringstream line (blokline); 
        std::string token;
        // activity name
        std::getline(line, token, ';');
        std::string name = cleanSpace(token);
        // activity capacity
        std::getline(line, token, ';');
        int capacity = convertToNumber(token);

        if (capacity < 0) {
            throw invalid_argument("Wrong capacity reading");
        }

        mActivities.insert({name, Activity(name, capacity)} );

        // cerr << Activity(name, capacity) << endl;

        return true;
    }
    void debPrintAskers() {
        while (!mAskers.empty())
        {
            mAskers.front().print();
            mAskers.pop();
        }
    }

    bool asignPeople () {

        while (! mAskers.empty() )
        {
            Person asker = mAskers.front();
            mAskers.pop();

            bool foundActivity = false;
            for (auto preference : asker.mPreferences) {

                auto activity = mActivities.find( preference );

                cout << "<" << preference << ">" << endl;
                if (activity == mActivities.end()) {
                    asker.print();
                    string ermes = "Preference '";
                    ermes.append(preference);
                    ermes.append("'does not match known Activity");
                    throw invalid_argument( ermes );
                }

                if ( activity->second.addPerson(asker) ) {
                    foundActivity = true;
                    break;
                }

            }
            if (foundActivity == false) {
                std::cout << "No match for: " << asker << endl;
            }

        }

        return true;

    }

    void outputActivities () const {

        int personCount = 0;

        for (auto activity : mActivities) {
            std::string outfilepath = "export/";
            outfilepath.append(activity.second.mName);
            outfilepath.append(".csv");
            ofstream outfile (outfilepath);
            if ( ! outfile.is_open() ) {
                throw runtime_error("Unable to output file");
            }

            for (auto pers : activity.second.mAtendees) {
                outfile << pers << endl;
                ++personCount;
            }
        }

        cout << "Export successful" << endl;
        cout << "matched: " << personCount << " people" << endl; 
    }
};

int main ( void) {

    Sorter dialog;

    dialog.readData();
    // dialog.debPrintAskers();
    dialog.asignPeople();
    dialog.outputActivities();

    return EXIT_SUCCESS;
}