function varargout = Kmeans_GUI(varargin)
% KMEANS_GUI MATLAB code for Kmeans_GUI.fig
%      KMEANS_GUI, by itself, creates a new KMEANS_GUI or raises the existing
%      singleton*.
%
%      H = KMEANS_GUI returns the handle to a new KMEANS_GUI or the handle to
%      the existing singleton*.
%
%      KMEANS_GUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in KMEANS_GUI.M with the given input arguments.
%
%      KMEANS_GUI('Property','Value',...) creates a new KMEANS_GUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Kmeans_GUI_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Kmeans_GUI_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Kmeans_GUI

% Last Modified by GUIDE v2.5 16-Nov-2017 16:48:14

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Kmeans_GUI_OpeningFcn, ...
                   'gui_OutputFcn',  @Kmeans_GUI_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Kmeans_GUI is made visible.
function Kmeans_GUI_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Kmeans_GUI (see VARARGIN)

% Choose default command line output for Kmeans_GUI
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Kmeans_GUI wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Kmeans_GUI_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
K = str2num(get(handles.edit2,'String'));
while (1)
    [data_set, class, err] = kmeans_fun(K);
    if any(isnan(err))
        continue
    else
        break
    end
end
% title('K-means')
% xlabel('x')
% ylabel('y')
if K == 1
   plot(handles.axes1, data_set(:,1), data_set(:,2), 'r*') 
end
if K == 2
    for p = 1:length(class)
       if class(p) == 1
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'r*')
           hold on
       else
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'b*') 
           hold on
       end
    end
    hold off
end
if K == 3
    for p = 1:length(class)
       if class(p) == 1
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'r*') 
           hold on
       elseif class(p) == 2
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'b*') 
           hold on
       else
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'y*') 
           hold on
       end
    end
    hold off
end
if K == 4
    for p = 1:length(class)
       if class(p) == 1
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'r*')
           hold on
       elseif class(p) == 2
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'b*') 
           hold on
       elseif class(p) == 3
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'y*') 
           hold on
       else
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'g*')
           hold on
       end
    end
    hold off
end

if K == 5
    for p = 1:length(class)
       if class(p) == 1
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'r*') 
           hold on
       elseif class(p) == 2
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'b*')
           hold on
       elseif class(p) == 3
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'y*') 
           hold on
       elseif class(p) == 4
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'g*') 
           hold on
       else
           plot(handles.axes1, data_set(p,1), data_set(p,2), 'k*')
           hold on
       end
    end
    hold off
end


function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% K = str2int(get(handles.edit2,'String'));
data_set = data_generation();
% axes()
% plot(handles.axes1,[0.5],[0.5],'r*');
plot(handles.axes1,data_set(:,1),data_set(:,2),'r*')
